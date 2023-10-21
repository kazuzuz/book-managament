from django import forms

class ReviewForm(forms.Form):
    review_text = forms.CharField(max_length=256)
    score = forms.IntegerField(max_value=5)
    
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
