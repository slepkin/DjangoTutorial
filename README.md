First Django project, following the [tutorial](https://docs.djangoproject.com/en/1.5/intro/).

### Routes
```
/ => expenses#index
/new => expenses#new
```

### Notes

Since this project only includes one table, a relational
database like PostgreSQL or SQLite3 is completely unnecessary.
I used one anyways, since I didn't want to be learning TOO many new
things at once.

For the sake of education, an effort was made to
compromise between using all the "magic" at our disposal,
and none of it. For example, the use of `django.shortcuts.render`,
but not `ModelForm`. This forced me to handle validations myself,
which is probably healthy... exactly once.

I used `django.contrib.messages` to implement a Flash that
informs the user how he failed validations. I can't for the life of life
of me figure out a way to extract the field name that each error message
refers to. There has to be a nice Exception attribute for it, but the
Python API isn't any help there.

The 'create' view is a bit of a mess, since I tried to put
all the business logic in it, to tidy up the template.

There has to be a better place to write all the `import` statements,
at the top of `views.py`.
