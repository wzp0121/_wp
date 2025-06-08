參考老師的程式再加上問ai後寫出來的
@app.post("/delete_post/{post_id}")
async def delete_post(
    post_id: int, 
    request: Request,
    db: Session = Depends(get_db)
):
    # 檢查使用者是否已登入
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="You must be logged in to delete a post")
    
    # 先檢查該貼文是否存在
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # 確認貼文是否屬於當前使用者
    if post.username != user["username"]:
        raise HTTPException(status_code=403, detail="You can only delete your own posts")
    
    # 刪除貼文
    db.delete(post)
    db.commit()
    
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)