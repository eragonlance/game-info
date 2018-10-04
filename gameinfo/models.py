from django.db import models

# Create your models here.
class Platform(models.Model):
    """ A gaming platform (Windows, Mac, PS4,...) """

    name = models.CharField(max_length=100, primary_key=True)
    shortName = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    """ A video game developer (company) """

    name = models.CharField(max_length=100, primary_key=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    """ A video game publisher """

    name = models.CharField(max_length=100, primary_key=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """ A video game genre (Action, Adventure, Fantasy,...) """

    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    """ A video game """

    name = models.CharField(max_length=100)
    homepage = models.URLField(blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    engine = models.CharField(max_length=20, blank=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


class Release(models.Model):
    """
    A release of a video game. A game can have multiple releases for
    different platforms with different release dates.
    """

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    platforms = models.ManyToManyField(Platform)
    date_released = models.DateField()

    def getPlatformString(self):
        # pylint: disable=no-member
        return ", ".join(str(p) for p in self.platforms.all())

    def __str__(self):
        return f"{self.game} - {self.date_released} - {self.getPlatformString()}"


class Url(models.Model):
    """ A related URL of a game """

    YOUTUBE = "youtube.com"
    METACRITIC = "metacritic.com"
    WIKIPEDIA = "en.wikipedia.org"

    ALLOWED_DOMAINS = (
        (YOUTUBE, "Youtube"),
        (METACRITIC, "Metacritic"),
        (WIKIPEDIA, "Wikipedia"),
    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    domain = models.URLField(choices=ALLOWED_DOMAINS)
    url = models.URLField()

    def __str__(self):
        return f"{self.game} - {self.domain}: {self.url}"
