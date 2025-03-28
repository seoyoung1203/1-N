```shell
def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)  # POST 요청으로 전달된 데이터를 기반으로 폼 객체를 생성
        if form.is_valid():  # 폼이 유효한지 검사
            comment = form.save(commit=False)  # 폼 데이터를 모델 인스턴스로 저장하지만 아직 데이터베이스에 저장하지 않음
** commit=False**는 데이터베이스에 저장하지 않고, 모델 인스턴스만 반환
   
   -> 폼의 save() 메서드 >> 모델을 바로 데이터베이스에 저장. 
   그러나 댓글의 article 필드는 외래 키로 게시물(Article)과 연결되어야 함. 
   이 필드는 폼을 통해 제출되지 않기 때문에, 저장 전에 해당 필드를 수동으로 설정.

=> commit=False를 사용하면, 댓글을 데이터베이스에 저장하기 전에 필요한 필드를 수정할 수 있음. 그런 후 save()를 호출하여 최종적으로 데이터베이스에 저장
           
            # 해당 article_id를 통해 댓글이 속할 게시물(Article) 가져오기
            article = Article.objects.get(id=article_id)

            # 댓글의 article 필드를 해당 게시물로 설정
            comment.article = article
         
            comment.save()  # 댓글을 데이터베이스에 저장

            # 댓글 작성 후 해당 게시물의 상세 페이지로 리다이렉트
            return redirect('articles:detail', id=article_id)
    else:
        # 만약 GET 요청이 들어오면, 댓글 작성이 아닌 다른 페이지로 리다이렉트
        return redirect('articles:index')
    ```
    ```shell
    <form action="{% url 'articles:comment_create' article.id %}" method="POST">
        {% csrf_token %}
        {{form}}
     <input type="text" class="form-control">
        <input type="submit">
    ```
    {{form}}이 있으니까 댓글 입력칸 있을텐데 왜 적었을까?
