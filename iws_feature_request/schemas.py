from .models import ma, FeatureRequest, Client, ProductArea


class FeatureRequestSchema(ma.ModelSchema):
    class Meta:
        model = FeatureRequest


class ClientSchema(ma.ModelSchema):
    class Meta:
        model = Client


class ProductAreaSchema(ma.ModelSchema):
    class Meta:
        model = ProductArea
