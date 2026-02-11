from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):

        # Drop collections directly to avoid Djongo PK issues
        from django.db import connection
        with connection.cursor() as cursor:
            for coll in ['activity', 'workout', 'leaderboard', 'user', 'team']:
                try:
                    cursor.execute(f'drop collection {coll}')
                except Exception:
                    pass

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        tony = User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel, is_superhero=True)
        steve = User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel, is_superhero=True)
        bruce_m = User.objects.create(email='bruce@marvel.com', name='Bruce Banner', team=marvel, is_superhero=True)
        clark = User.objects.create(email='clark@dc.com', name='Clark Kent', team=dc, is_superhero=True)
        bruce_w = User.objects.create(email='bruce@dc.com', name='Bruce Wayne', team=dc, is_superhero=True)
        diana = User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc, is_superhero=True)

        # Create activities
        Activity.objects.create(user=tony, activity_type='Running', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Cycling', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=bruce_m, activity_type='Swimming', duration_minutes=60, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Running', duration_minutes=25, date=timezone.now().date())
        Activity.objects.create(user=bruce_w, activity_type='Cycling', duration_minutes=35, date=timezone.now().date())
        Activity.objects.create(user=diana, activity_type='Swimming', duration_minutes=50, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flying heroes')
        w1.suggested_for.set([tony, steve, bruce_m])
        w2.suggested_for.set([clark, bruce_w, diana])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=300)
        Leaderboard.objects.create(team=dc, total_points=250)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
