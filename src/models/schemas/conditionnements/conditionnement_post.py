from ...bases.conditionnement import ConditionnementBase


class ConditionnementPost(ConditionnementBase):

    """Schéma Conditionnement pour création en base de données"""
 
    # FIXME : Décommenter après avoir créer les autres tables !
    #objets: List["ObjetCond"] = Relationship(back_populates="condit")
    pass