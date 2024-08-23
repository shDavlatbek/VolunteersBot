from django import forms
from .models import Guest, Message, Category, User

class MessageForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.SelectMultiple,  # or another widget
        label="Categories"
    )
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.SelectMultiple,  # or another widget
        label="Users"
    )

    class Meta:
        model = Message
        fields = ['title', 'message', 'categories', 'users']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Pre-populate the fields with existing data
            self.fields['users'].initial = self.instance.user.all()
            # Assuming Category has a relationship to User that you can reverse
            self.fields['categories'].initial = self.instance.categories.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        selected_categories = self.cleaned_data.get('categories')
        users = self.cleaned_data.get('users')
        if selected_categories:
            selected_users = User.objects.none()
            # Assuming your User model is related to the Category model
            for category in selected_categories:
            # Filter Guests by category and then get the associated Users
                users_in_category = User.objects.filter(guests__in=Guest.objects.filter(categories=category))
                selected_users = selected_users | users_in_category | users  # Combine querysets of users

            # Remove duplicates (if any) by using distinct() 
            selected_users = selected_users.distinct()
            instance.user.set(selected_users)
        if commit:
            instance.save()
        return instance