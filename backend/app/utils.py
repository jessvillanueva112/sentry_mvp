def to_dict(model_instance):
    """Convert a SQLAlchemy model instance into a dictionary."""
    return {c.name: getattr(model_instance, c.name) for c in model_instance.__table__.columns}