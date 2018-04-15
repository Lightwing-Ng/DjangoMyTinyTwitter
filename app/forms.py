#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 11:31 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""

from django.forms import ModelForm, ValidationError
from app.models import Moment


class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'
        # 将所有模型类中的字段导入表单中

    def clean(self):
        cleaned_data = super(MomentForm, self).clean()
        content = cleaned_data.get("content")
        if content is None:
            raise ValidationError(
                "请输入Content内容!"
            )
        elif content.find("ABCD") >= 0:
            raise ValidationError(
                "不能输入敏感字 ABCD !"
            )
