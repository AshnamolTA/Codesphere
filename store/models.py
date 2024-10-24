from django.db import models


from django.contrib.auth.models import User

from embed_video.fields import EmbedVideoField

# Create your models here.


class BaseModel(models.Model):

    created_date=models.DateTimeField(auto_now_add=True)
    
    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)


class UserProfile(BaseModel):

    bio=models.CharField(max_length=200)

    profile_picture=models.ImageField(upload_to="profile_picture",null=True,blank=True)

    phone=models.CharField(max_length=200)

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")


    def __str__(self):

        return self.owner.username





class Tag(BaseModel):

    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title




class Project(BaseModel):

    title=models.CharField(max_length=200)

    description=models.TextField()

    preview_image=models.ImageField(upload_to="previewimage",null=True,blank=True)

    price=models.PositiveIntegerField()

    developer=models.ForeignKey(User,on_delete=models.CASCADE)

    files=models.FileField(upload_to="project",null=True,blank=True)

    tag_objects=models.ManyToManyField(Tag)

    thumbnail=EmbedVideoField


#whishlist.objects.filter(owner=request.user)

#request.user.basket
class WishList(BaseModel):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="basket")


class WishListItem(BaseModel):

    wishlist_object=models.ForeignKey(WishList,on_delete=models.CASCADE,related_name="basket_item")

    project_object=models.ForeignKey(Project,on_delete=models.CASCADE)

    is_order_placed=models.BooleanField(default=False)


class Order(BaseModel):

    wishlistitem_objects=models.ManyToManyField(WishListItem)

    is_paid=models.BooleanField(default=False)

    order_id=models.CharField(max_length=200,null=True)
