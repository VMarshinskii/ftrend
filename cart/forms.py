# -*- coding: utf-8 -*-
from django import forms
from models import CartProduct


class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['count', 'size', 'color']