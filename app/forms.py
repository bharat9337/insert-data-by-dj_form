from django import forms


def validate_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('Bcoz starts with a') 
    
def validate_for_len(data):
    if len(data) < 5 :
        raise forms.ValidationError('Required Minimum 5 Characters ')



class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_a])
    Sprincipal=forms.CharField(validators=[validate_for_len])
    Slocation=forms.CharField()
    email=forms.EmailField()
    renteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)




    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('BOT')



    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['renteremail']

        if e !=re:
            raise forms.ValidationError('Emails not Matched')