import React, { useState } from 'react';

const FileUpload = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
	setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
	event.preventDefault();
	if (!file) {
  	alert('Please select a file to upload');
  	return;
	}

	const formData = new FormData();
	formData.append('file', file);

	try {
  	const response = await fetch('http://127.0.0.1/upload', {
    	method: 'POST',
    	body: formData,
  	});

  	if (!response.ok) {
    	throw new Error('Network response was not ok');
  	}

  	const data = await response.json();
  	console.log('File uploaded successfully:', data);
	} catch (error) {
  	console.error('Error uploading file:', error);
	}
  };

  return (
    
	<form onSubmit={handleSubmit} id="filelook">
  	<input type="file" onChange={handleFileChange}/>
  	<button type="submit" id="submitlook">Upload File</button>
	</form>
    
  );
};

export default FileUpload;
