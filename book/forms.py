from django import forms

#ModelForm
#form.review_textでインプットを表示させる

class ReviewForm(forms.Form):
    review_text = forms.CharField(max_length=256,
                                  widget=forms.Textarea(attrs={'rows': 10,
                                                               'cols': 50, 
                                                               'class': 'custom-textarea'}))
    score = forms.IntegerField(max_value=5, min_value=0)
    
    review_title = forms.CharField(max_length=256)
    
    def clean_review_text(self):
        review_text = self.cleaned_data.get("review_text")
        if len(review_text) >= 255:
            raise forms.ValidationError("文字が多すぎます")
        return review_text

    def clean_score(self):
        score = self.cleaned_data.get("score")
        if (score < 0 or 5 < score) :
            raise forms.ValidationError("スコアは0から5の整数で入力してください。")
        return score
