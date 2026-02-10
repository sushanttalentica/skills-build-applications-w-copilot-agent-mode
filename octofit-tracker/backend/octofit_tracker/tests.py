from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T')
        u = User.objects.create(email='a@b.com', name='A', team=team)
        self.assertEqual(str(u), 'a@b.com')
    def test_activity_create(self):
        team = Team.objects.create(name='T')
        u = User.objects.create(email='a@b.com', name='A', team=team)
        a = Activity.objects.create(user=u, activity_type='Run', duration_minutes=10, date='2024-01-01')
        self.assertIn('Run', str(a))
    def test_workout_create(self):
        w = Workout.objects.create(name='W')
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T')
        l = Leaderboard.objects.create(team=team, total_points=5)
        self.assertIn('T', str(l))
