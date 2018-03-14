==================
django-media-tools
==================

django-media-tools is an app that provides useful widgets for managing media files in django admin. It doesn't use any javascript library.

Works with Django 1.10 and newer versions.

Installation
============

#. Install using pip::

    pip install django-media-tools

#. Add ``media_tools`` to the ``INSTALLED_APPS``::

    INSTALLED_APPS = [
       ...
       'media_tools',
    ]

#. Run ``collectstatic`` command. It will copy the static files used by media_tools to your static root.::

     python manage.py collectstatic


PreviewImageWidget
==================

PreviewImageWidget is a fairly simple widget that you can use for previewing an ``ImageField``.
The image-box is located at left of the Browse button as you can see below. If you click the image-box you will notice that the image will be open in a modal-box with a bigger size.

**image-box**: preview of the image

**modal-box**: it pops up when you click on the image-box

.. image:: https://screenshotscdn.firefoxusercontent.com/images/c7cce7f5-cfe6-4de0-9d1b-1dc9529c87f4.png

**Settings for PreviewImageWidget**

Add ``DJANGO_MEDIA_TOOLS_CONFIG`` to your ``settings.py`` file if you want to set defaults for PreviewImageWidget. ::

    DJANGO_MEDIA_TOOLS_CONFIG = {
        # max sizes of preview image-box
        'preview_max_height': '150px',
        'preview_max_width': '150px',

        # max size of preview modal-box (the box that is opened when clicked on image)
        'preview_modal_max_height': '90%',
        'preview_modal_max_width': '90%',

        # Hides 'currently' label on admin
        'hide_currently': False,

        # Shows the image url at the bottom of the modal if set to True
        'show_caption': True
    }

**How to use PreviewImageWidget**

sample *models.py* ::

    class Product(models.Model):
        name = models.CharField(_('name'), max_length=50)
        photo = models.ImageField(_('Photo'), upload_to='testing/product', blank=True)
        banner = models.ImageField(_('Banner'), upload_to='testing/product', blank=True)


sample *forms.py* ::

    from media_tools.widgets import ImagePreviewWidget
    from .models import Product

    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = '__all__'
            widgets = {
                'photo': ImagePreviewWidget(preview_max_height='80px', preview_modal_max_height='600px', hide_currently=True, ),
                'banner': ImagePreviewWidget(preview_max_width='150px', preview_modal_max_width='50%', show_caption=False),
            }

As you can see you can override the default settings by giving them as kwargs.