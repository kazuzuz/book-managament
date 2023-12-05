from django import forms

#ModelForm
#form.review_textでインプットを表示させる

class Search_selection(forms.Form):
    CHOICE = [
        ('title', '作品'),
        ('author', '著者'),
    ]
    
    one = forms.ChoiceField(
        label='検索対象',
        choices=CHOICE,
        initial='title',
        required=True,
        widget=forms. SelectMultiple(attrs={
               'id': 'one',})
    )
        
    