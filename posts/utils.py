from django.utils.text import slugify
# from django.conf import settings

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''
import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

# def compatible_staticpath(path):
#     '''
#     Try to return a path to static the static files compatible all
#     the way back to Django 1.2. If anyone has a cleaner or better 
#     way to do this let me know!
#     '''
#     try:
#         # >= 1.4
#         from django.templatetags.static import static
#         return static(path)
#     except ImportError:
#         pass
#     try:
#         # >= 1.3
#         return '%s/%s' % (settings.STATIC_URL.rstrip('/'), path)
#     except AttributeError:
#         pass
#     try:
#         return '%s/%s' % (settings.PAGEDOWN_URL.rstrip('/'), path)
#     except AttributeError:
#         pass
#     return '%s/%s' % (settings.MEDIA_URL.rstrip('/'), path)