from django.db import models


class Mapcenter(models.Model):
	"""地图中心"""
	cityname = models.CharField(max_length=20)
	def _str_(self):
		"""返回模型的字段"""
		return self.cityname

class Userpoi(models.Model):
    upoiname=models.CharField(max_length=20)
    upoilog =models.CharField(max_length=20)
    upoilat =models.CharField(max_length=20)
    def _str_(self):
        return self.upoiname

"""L"""
class Topic(models.Model):
    """城市名称"""
    text = models.CharField(max_length=200)

    def _str_(self):
        """返回模型的字符串表示"""
        return self.text
class Entry(models.Model):
    """城市下的poi信息"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)#引用了数据库中的另一条记录，将每个条目关联到特定的城市
    text = models.TextField()#表示字段不需要长度限制
    #poi的名称
    # name =models.TextField()
    # #poi的经度
    # longitude=models.TextField()
    # #poi的纬度
    # latitude=models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:#Meta存储用于管理模型的额外信息
        verbose_name_plural = 'entries'
    def _str_(self):#呈现条目时应显示哪些信息
        """返回模型的字符串表示"""
        return self.text[:50] + "..."
"""L"""