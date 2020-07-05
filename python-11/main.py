from api.models import User, Agent, Event, Group
from datetime import datetime, timedelta


def get_active_users() -> User:
    active = User.objects.filter(
        last_login__gte = (
            datetime.today() - timedelta(10)
        )
    )
    return active


def get_amount_users() -> User:
    users = User.objects.count()
    return users


def get_admin_users() -> User:
   admins = User.objects.filter(group__name='admin')
   return admins


def get_all_debug_events() -> Event:
    events = Event.objects.filter(level='debug')
    return events


def get_all_critical_events_by_user(agent) -> Event:
    critical = Event.objects.filter(level='critical', agent=agent)
    return critical


def get_all_agents_by_user(username) -> Agent:
    agent = Agent.objects.filter(user__name=username)
    return agent


def get_all_events_by_group() -> Group:
   group = Group.objects.filter(user__agent__event__level = 'information')
   return group
