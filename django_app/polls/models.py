from django.db import models


class Question(models.Model):
    question_text = models.CharField('질문내용', max_length=200)
    pub_date = models.DateTimeField('발행일자')


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name='해당 질문',
        on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Model : DB와 데이터 송수신을 위한 모듈
    # Model에 생성한 클래스에서 사용하는 변수는 DB 테이블의 컬럼과 일치해야 함
    # ForeignKey dml 필드명은 verbose_name 옵션에 넣어줘야 함.
