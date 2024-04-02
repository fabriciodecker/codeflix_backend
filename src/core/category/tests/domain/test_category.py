import pytest
from uuid import UUID
import uuid


from src.core.category.domain.category import Category

class TestCategory():
    # usando pytest
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"): 
            Category()
            
    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name cannot be longer than 255"):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid_by_Default(self):
        category = Category(name="Filme")
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.description == ""
        assert category.is_active is True

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Filme")
        assert category.is_active is True

    def test_category_is_create_with_provided_values(self):
        cat_id = uuid.uuid4()
        category = Category(
            id=cat_id,
            name="Filme",
            description="Filmes em geral",
            is_active=False,
        )
        assert category.id == cat_id
        assert category.name == "Filme"
        assert category.description == "Filmes em geral"
        assert category.is_active is False

    def test_str(self):
        cat = Category(name="Filme")
        assert str(cat), f"{cat.name} - {cat.description} ({cat.is_active})"

    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")

  # Não consegui resolver. Tem aspas simples na segunda string que não sei como tirar ou adicionar na primeira string
        # AssertionError: <Category Filme (bb1acf2c-8cc9-40f3-96a5-c50f525cf4ee) != '<Category Filme (bb1acf2c-8cc9-40f3-96a5-c50f525cf4ee)'"
    # def test_rep(self):
    #     cat = Category(name="Filme", id="bb1acf2c-8cc9-40f3-96a5-c50f525cf4ee")
    #     self.assertEqual(cat, "<Category {} ({})>".format(cat.name, cat.id))

class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        cat = Category(name = "Filme", description="Filmes em geral")
        cat.update_category(name= "Série", description="Séries em geral")
        assert cat.name == "Série"
        assert cat.description == "Séries em geral"

    def test_cannot_update_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")

class TestActivate:
    def test_activate_category(self):
        cat = Category(name = "Filme", description="Filmes em geral", is_active=False)
        cat.activate()
        assert cat.is_active is True

    def test_deactivate_category(self):
        cat = Category(name = "Filme", description="Filmes em geral", is_active=True)
        cat.deactivate()
        assert cat.is_active is False


class TestEquality:
    def test_when_categories_have_same_id_they_are_equal(self):
        common_id = uuid.uuid4()
        cat1 = Category(name="Filme", id=common_id)
        cat2 = Category(name="Filme", id=common_id)
        assert cat1 == cat2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id = uuid.uuid4
        cat = Category(name="Filme", id=common_id)
        dummy = Dummy()
        dummy.id = common_id

        assert Category != dummy







  


#para rodar, no terminal
    # pytest /home/fdc/certi/sistemas/cursos/full-cycle/python/codeflix-catalog-admin
        
# ou configurar no vscode testes - feito
        