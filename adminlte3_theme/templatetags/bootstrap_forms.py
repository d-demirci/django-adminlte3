from django.contrib.admin.widgets import RelatedFieldWidgetWrapper, AdminSplitDateTime, AdminFileWidget
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.filter(is_safe=True)
def bootstrap_input(value):
    """Adds appropriate bootstrap CSS classes to widgets so that they are rendered bootstrap-ish"""
    current_classes = value.field.widget.attrs.get("class", "").strip().split(" ")
    field_type = value.field.widget.attrs.get("type", "text")

    print(type(value.field.widget))

    if field_type == "range":
        bootstrap_class = "form-control-range"
    elif field_type == "checkbox" or field_type == "radio":
        bootstrap_class = "form-check-input"
    elif field_type == "file":
        bootstrap_class = "custom-file-input"
    elif isinstance(value.field.widget, RelatedFieldWidgetWrapper):
        bootstrap_class = "custom-select"  # For wrapped widgets (those with edit, add and delete icons)
    elif isinstance(value.field.widget, AdminFileWidget):
        bootstrap_class = "custom-file-input"
    elif isinstance(value.field.widget, AdminSplitDateTime):
        return value  # We don't want to style the date time field (for now)
    else:
        bootstrap_class = "form-control"

    # We always have a list. This checks if first item contains something (list is not [''], meaning the attribute
    # contained something) and then adds the bootstrap_class if it is not already there. If the list is "empty" then we create
    # a new one that contains only the bootstrap_class we want.
    if current_classes[0] and bootstrap_class not in current_classes:
        current_classes.append(bootstrap_class)
    else:
        current_classes = [bootstrap_class]
    
    # Also add the is-invalid class to render the field with a red border if there are any errors.
    if value.errors:
        current_classes.append("is-invalid")

    return value.as_widget(attrs={"class": " ".join(current_classes)})
