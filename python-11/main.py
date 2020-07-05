from api.models import User, Agent, Event, Group
from datetime import datetime, timedelta


def get_active_users() -> User:
    now = datetime.today()
    active_users = User.objects.filter(
        last_login_gte = (
            now - timedelta(10)
        )
    )
    return active_users


def get_amount_users() -> User:
    all_users = User.objects.count()
    return all_users


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    raise NotImplementedError


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    raise NotImplementedError


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    raise NotImplementedError


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    raise NotImplementedError


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    raise NotImplementedError
