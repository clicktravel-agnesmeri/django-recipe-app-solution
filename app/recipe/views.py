from core.models import Ingredient

from recipe import serializers


class IngredientViewSet():
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewSet():
    """Manage recipes in the database"""

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)
