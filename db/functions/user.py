from db.table import UsersTable, UsersWordsTable, LanguagsEnum
from db.engine import engine
from sqlalchemy.orm import sessionmaker


def register(telegram_id, first_name, last_name, learn_lang=1, translate_lang=2):
    """
    Register a user in the database
    """
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = UsersTable(telegram_id=telegram_id,
                          first_name=first_name, last_name=last_name,
                          word_learn=LanguagsEnum(int(learn_lang)),
                          word_translate=LanguagsEnum(int(translate_lang))
                          )
        session.add(user)
        session.commit()

    except Exception as e:
        print(e)


def get_user_data(telegram_id):
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(UsersTable).filter(
        UsersTable.telegram_id == telegram_id).first()
    return result if result else None

def user_data_reset(telegram_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    user = session.query(UsersTable).filter(
        UsersTable.telegram_id == telegram_id).first()
    session.query(UsersWordsTable).filter(
        UsersWordsTable.user_id == user.id
    ).delete()
    session.commit()

def get_user_lang(telegram_id):
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(UsersTable).filter(
        UsersTable.telegram_id == telegram_id).first()
    return result.word_learn, result.word_translate if result else None