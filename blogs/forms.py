from django import forms
from .models import Blogs

class Createnewpost(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('article_header','article_description','article_banner','first_header','first_description','first_image','second_header','second_description','second_image','third_header','third_description','third_image','fourth_header','fourth_description','fourth_image','fifth_header','fifth_description','fifth_image','sixth_header','sixth_description','sixth_image','seventh_header','seventh_description','seventh_image','eighth_header','eighth_description','eighth_image','ninth_header','ninth_description','ninth_image','tenth_header','tenth_description','tenth_image')
