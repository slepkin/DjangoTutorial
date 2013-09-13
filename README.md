First Django project, following the [tutorial](https://docs.djangoproject.com/en/1.5/intro/).

### Notes

Since this project only includes one table, a relational
database like PostgreSQL or SQLite3 are completely unnecessary.
I used them anyways, since I didn't want to be learning TOO many
things at once.

For the sake of education, an effort was made to
compromise between using all the "magic" at our disposal,
and none of it. For example, the use of
`django.shortcuts.render`, but not `ModelForm`. This forced
me to handle validations myself, which is probably healthy...
exactly once.

I used `django.contrib.messages` to implement a Flash that
informs the user how he failed validations.
