from flask import request, abort, jsonify, Blueprint
import random

from flaskr.models import Question, Category

QUESTIONS_PER_PAGE = 5
trivia = Blueprint('trivia', __name__)


@trivia.route('/categories/')
def retrieve_categories():
    """
    Get a list of categories
    :return: a list of categories
    """
    categories = Category.query.all()

    if len(categories) == 0:
        abort(404)

    return jsonify({
        'success': True,
        'categories': {category.id: category.type for category in categories}
    })


@trivia.route('/categories/<int:category_id>/', methods=['GET'])
def retrieve_category(category_id):
    """
    Get a list of categories
    :return: a list of categories
    """
    try:
        category = Category.query.get(category_id)

        return jsonify({
            'success': True,
            'category_type': category.type,
        })

    except:
        abort(404)


@trivia.route('/categories/', methods=['POST'])
def add_catagory():
    """
    Adds a category
    :return: Id of the question that has been created
    """
    body = request.get_json()

    if not ('type' in body):
        abort(422)

    try:
        category = Category(type=body.get('type')
                            )
        category.insert()
        return jsonify({
            'success': True,
            'created': category.id,
        })
    except:
        abort(422)


@trivia.route('/questions/')
def retrieve_questions():
    """
    Get a list of questions
    :return: a list of questions
    """
    page = request.args.get('page', 1)

    questions = Question.query.order_by(
        Question.id).paginate(int(page), per_page=QUESTIONS_PER_PAGE)
    categories = Category.query.order_by(Category.type).all()

    if questions.total == 0:
        abort(404)

    return jsonify({
        'success': True,
        'questions': [question.format() for question in questions.items],
        'total_questions': questions.total,
        'categories': {category.id: category.type for category in categories},
        'current_category': None
    })


@trivia.route('/questions/<int:question_id>/', methods=['GET'])
def retrive_question(question_id):
    """
    Delete a question using question id
    :param question_id: Id of the question to be deleted
    :return: Id of the question that has been deleted
    """
    try:
        question = Question.query.get(question_id)
        category = Category.query.get(question.category)
        return jsonify({
            'success': True,
            'question': question.format(),
            'category': category.type
        })
    except:
        abort(404)


@trivia.route('/questions/<int:question_id>/', methods=['DELETE'])
def delete_question(question_id):
    """
    Delete a question using question id
    :param question_id: Id of the question to be deleted
    :return: Id of the question that has been deleted
    """
    try:
        question = Question.query.get(question_id)
        question.delete()
        return jsonify({
            'success': True,
            'deleted': question_id
        })
    except:
        abort(422)


@trivia.route('/questions/', methods=['POST'])
def add_question():
    """
    Adds a question
    :return: Id of the question that has been created
    """
    body = request.get_json()

    if ('question' not in body) or ('answer' not in body) or \
            ('difficulty' not in body) or ('category' not in body):
        abort(422)

    try:
        question = Question(question=body.get('question'),
                            answer=body.get('answer'),
                            difficulty=body.get('difficulty'),
                            category=body.get('category'),
                            )
        question.insert()
        return jsonify({
            'success': True,
            'created': question.id,
        })
    except:
        abort(422)


@trivia.route('/questions/search/', methods=['POST'])
def search_questions():
    """
    searches for text in questions
    :return: Id of the question that has been created
    """
    body = request.get_json()
    search_term = body.get('search_term', None)

    if search_term:
        search_results = Question.query.filter(
            Question.question.ilike(f'%{search_term}%')).all()

        return jsonify({
            'success': True,
            'questions': [question.format() for question in search_results],
            'total_questions': len(search_results),
            'current_category': None
        })
    abort(404)


@trivia.route('/categories/<int:category_id>/questions/', methods=['GET'])
def retrieve_questions_by_category(category_id):
    """
    Get a list of questions
    :param category_id: Id of the category to be searched
    :return: a list of questions
    """
    try:
        questions = Question.query.filter(
            Question.category == str(category_id)).all()
        return jsonify({
            'success': True,
            'questions': [question.format() for question in questions],
            'total_questions': len(questions),
            'current_category': category_id
        })

    except:
        abort(404)


@trivia.route('/quizzes/', methods=['POST'])
def play_quiz():
    """
    play trivia game
    """
    try:

        body = request.get_json()
        if not ('quiz_category' in body and 'previous_questions' in body):
            abort(422)

        category = body.get('quiz_category')
        previous_questions = body.get('previous_questions')

        if category['type'] == 'click':
            available_questions = Question.query.filter(
                Question.id.notin_((previous_questions))).all()
        else:
            available_questions = Question.query.filter_by(
                category=category['id']).filter(
                Question.id.notin_((previous_questions))).all()


        new_question = available_questions[random.randrange(
            0, len(available_questions))].format() if len(
            available_questions) > 0 else None

        return jsonify({
            'success': True,
            'question': new_question
        })
    except:
        abort(422)
