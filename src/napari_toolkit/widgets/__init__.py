from .acknowledgements import setup_acknowledgements
from .buttons.icon_button import setup_iconbutton
from .buttons.push_button import setup_pushbutton
from .buttons.radio_button import setup_radiobutton
from .buttons.toggle_button import setup_togglebutton
from .checkbox import setup_checkbox
from .color.color_picker import setup_colorpicker
from .color.colorbar import setup_colorbar
from .color.edit_color_picker import setup_editcolorpicker
from .combobox import setup_combobox
from .file_select import setup_dirselect, setup_fileselect, setup_savefileselect
from .icon_wrapper import setup_icon_wrapper
from .layer_select import setup_layerselect
from .progressbar.progress_edit import setup_progressbaredit
from .progressbar.progressbar import setup_progressbar
from .sliders.double_slider import setup_doubleslider
from .sliders.edit_slider import setup_editdoubleslider, setup_editslider
from .sliders.labeled_slider import setup_labeleddoubleslider, setup_labeledslider
from .sliders.slider import setup_slider
from .spinbox import setup_doublespinbox, setup_spinbox
from .switch import setup_hswitch, setup_vswitch
from .text_edit import setup_label, setup_lineedit, setup_plaintextedit, setup_textedit
from .timeedit import setup_timeedit

__all__ = [
    "setup_acknowledgements",
    "setup_pushbutton",
    "setup_radiobutton",
    "setup_togglebutton",
    "setup_checkbox",
    "setup_colorpicker",
    "setup_colorbar",
    "setup_editcolorpicker",
    "setup_combobox",
    "setup_dirselect",
    "setup_fileselect",
    "setup_savefileselect",
    "setup_layerselect",
    "setup_progressbaredit",
    "setup_progressbar",
    "setup_doubleslider",
    "setup_editdoubleslider",
    "setup_editslider",
    "setup_labeleddoubleslider",
    "setup_labeledslider",
    "setup_slider",
    "setup_doublespinbox",
    "setup_spinbox",
    "setup_hswitch",
    "setup_vswitch",
    "setup_label",
    "setup_lineedit",
    "setup_plaintextedit",
    "setup_textedit",
    "setup_timeedit",
    "setup_icon_wrapper",
    "setup_iconbutton",
]
