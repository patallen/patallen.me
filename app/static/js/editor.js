var editor = new EpicEditor({
    container: 'epiceditor',
    autogrow: true,
    textarea: 'text-area-editor',
    theme: {
        base: 'https://cdnjs.cloudflare.com/ajax/libs/epiceditor/0.2.2/themes/base/epiceditor.css',
        preview: 'https://cdnjs.cloudflare.com/ajax/libs/epiceditor/0.2.2/themes/preview/github.css',
        editor: 'https://cdnjs.cloudflare.com/ajax/libs/epiceditor/0.2.2/themes/editor/epic-light.css'
    }
}).load();