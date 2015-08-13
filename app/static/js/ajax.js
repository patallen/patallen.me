$(function(){
    $('.delete-project-btn').unbind('click').on('click', function(event){
        event.preventDefault();
        event.stopPropagation();
        deleteProjectAjax($(this));
    });
});

function deleteProjectAjax(obj){
    $project = obj.closest('.project');
    var projectId = $project.data('project-id');
    var conf = confirm("Are you sure you want to delete this project?");
    if(conf){
        $.ajax({
            url: '/portfolio/'+projectId,
            type: 'DELETE',
            success: function(res){
                $project.remove();
                console.log(res)
            },
            error: function(res){
                console.log(res)
            }
        })
    };
    
}