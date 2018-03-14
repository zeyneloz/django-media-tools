from django.conf import settings
from django.contrib.admin.widgets import AdminFileWidget


DEFAULT_IMAGE_PREVIEW_CONFIG = {
    'preview_max_height': '150px',
    'preview_max_width': '150px',
    'preview_modal_max_height': '90%',
    'preview_modal_max_width': '90%',
    'preview_widget_img_id': '_id',
    'preview_widget_modal_id': '_id',
    'preview_widget_modal_img_id': '_id',
    'preview_widget_modal_caption_id': '_id',
    'hide_currently': False,
    'show_caption': True
}


class ImagePreviewWidget(AdminFileWidget):
    template_name = 'media_tools/image-preview-widget.html'

    class Media:
        css = {
            'all': ('media_tools/css/image-preview-widget.css',)
        }
        js = ('media_tools/js/image-preview-widget.js',)

    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', None)
        super(ImagePreviewWidget, self).__init__(*args, attrs=attrs)
        self.config = DEFAULT_IMAGE_PREVIEW_CONFIG.copy()

        # Get defined values from the settings and update the default config
        conf = getattr(settings, 'DJANGO_MEDIA_TOOLS_CONFIG', {})
        self.config.update(conf)
        self.config.update(kwargs)

    def _update_element_id(self, name):
        self.config['preview_widget_img_id'] = 'preview-widget-img-%s' % name
        self.config['preview_widget_modal_id'] = 'preview-widget-modal-%s' % name
        self.config['preview_widget_modal_img_id'] = 'preview-widget-modal-img-%s' % name
        self.config['preview_widget_modal_caption_id'] = 'preview-widget-modal-caption-%s' % name

    def render(self, name, value, attrs=None, renderer=None):
        if not attrs:
            attrs = {}
        self._update_element_id(name)
        attrs.update({
            'class': 'preview-widget-file',
            'data-preview-widget-img': self.config['preview_widget_img_id']
        })
        return super(ImagePreviewWidget, self).render(name, value, attrs=attrs, renderer=renderer)

    def get_context(self, name, value, attrs):
        context = super(ImagePreviewWidget, self).get_context(name, value, attrs)
        context['widget'].update(self.config)
        return context
