KindEditor.ready(function(K) {
  /*
  K.create('textarea[name="descripcion"]',{
		resizeType : 1,
		allowPreviewEmoticons : false,
		allowImageUpload : false,
		items : [
			'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
			'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
			'insertunorderedlist', '|', 'image', 'link']
	});
*/
for(var els = document.getElementsByTagName ('textarea'), i = els.length; i--;)
    if (els[i].className == "mykindeditor")
      K.create('textarea[name='+els[i].name+']',{
    		resizeType : 1,
    		allowPreviewEmoticons : false,
    		allowImageUpload : false,
    		items : [
    			'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
    			'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
    			'insertunorderedlist', '|', 'image', 'link']
    	});


});
