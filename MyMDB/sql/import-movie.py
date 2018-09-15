from core.models import Movie

sleuth = Movie.objects.create(
    title = 'Sleuth',
    plot = 'An snobbish writer who loves games invites his wife\'s lover for a battle of wits.',
    year = 1972,
    runtime = 138,
)

sleuth.id
sleuth.get_rating_display()
