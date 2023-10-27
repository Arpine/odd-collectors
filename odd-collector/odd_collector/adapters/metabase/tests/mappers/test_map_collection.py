from odd_collector.adapters.metabase.domain import Collection
from odd_collector.adapters.metabase.generator import MetabaseGenerator
from odd_collector.adapters.metabase.mappers.collection import map_collection
from odd_models.models import DataEntityType


def test_collection():
    generator = MetabaseGenerator(host_settings="localhost")
    collection = Collection(
        id=1,
        name="test_collection",
        description="collection for test",
        slug="test_collection",
        archived=False,
        cards_id=[1],
        dashboards_id=[2],
        can_write=True,
    )

    data_entity = map_collection(collection, generator)

    assert data_entity.oddrn == "//metabase/host/localhost/collections/1"
    assert data_entity.type == DataEntityType.FILE
    assert len(data_entity.data_entity_group.entities_list) == 2
    assert (
        "//metabase/host/localhost/collections/1/cards/1"
        in data_entity.data_entity_group.entities_list
    )
    assert (
        "//metabase/host/localhost/collections/1/dashboards/2"
        in data_entity.data_entity_group.entities_list
    )
