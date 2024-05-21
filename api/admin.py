from    django.contrib  import  admin
import    api.models  as api_models

admin.site.register(api_models.Course)
admin.site.register(api_models.Teacher)
admin.site.register(api_models.Variant)
admin.site.register(api_models.VariantItem)
admin.site.register(api_models.Question_Answer)
admin.site.register(api_models.Question_Answer_Message)
admin.site.register(api_models.Cart)
admin.site.register(api_models.CartOrder)
admin.site.register(api_models.CartOrderItem)
admin.site.register(api_models.Certificate)
admin.site.register(api_models.Category)
