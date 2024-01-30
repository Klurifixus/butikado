from django import forms
from .models import BlogPost, SubCategory

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subcategory', 'image', 'youtube_video_url', 'uploaded_video', 'content']

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)

        # Setting up the querysets and widgets for the form fields
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        
        # Subcategory field: dropdown of available subcategories
        self.fields['subcategory'].queryset = SubCategory.objects.all()
        self.fields['subcategory'].widget.attrs.update({'class': 'form-control'})

        # Image field: using a FileInput widget
        self.fields['image'].widget = forms.FileInput(attrs={'class': 'form-control-file'})

        # YouTube video URL field
        self.fields['youtube_video_url'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter a valid YouTube video URL (optional)',
            'help_text': 'Example: https://www.youtube.com/watch?v=YOUR_VIDEO_ID'
        })

        # Set youtube_video_url as optional (not required)
        self.fields['youtube_video_url'].required = False

        # Uploaded video field: using a FileInput widget
        self.fields['uploaded_video'].widget = forms.FileInput(attrs={'class': 'form-control-file'})

        # Content field: using a Textarea widget
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
