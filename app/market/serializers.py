from rest_framework import serializers


class PricesSerilizer(serializers.Serializer):
    open_price = serializers.CharField( max_length=255)
    higher_price = serializers.CharField(max_length=255)
    lower_price = serializers.CharField(max_length=255)
    variation = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
        return representation

class PricesDailySerilizer(serializers.Serializer):
    date = serializers.CharField(max_length=255)
    pirce = PricesSerilizer()

