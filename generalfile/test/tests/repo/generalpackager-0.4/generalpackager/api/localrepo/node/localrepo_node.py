
from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.localrepo.node.metadata_node import Metadata_Node


class LocalRepo_Node(LocalRepo):
    cls_target = LocalRepo.Targets.node
    cls_metadata = Metadata_Node

