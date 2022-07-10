from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Catalog_Urls


class RegUsers(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

class InOutLink(forms.ModelForm):
    class Meta:
        model = Catalog_Urls
        fields = ['long_link']


    def isvalid(self, data, form):
        dt = list([v for v in data.values()])[1]
        if dt[0] == "{" and dt[-1] == "}":
            print("form don't valid")
        form.is_valid()


# <form name="test" method="post" action="input1.php">
#     <p><b>Вставьте url адрес в поле</b><br>
#         <input type="text" size="40">
#     </p>
#     <button type="submit">Создать</button>
#     <p><b>Ваш короткий url</b><br>
#         <input type="text" size="40">
#     </p>
# </form>