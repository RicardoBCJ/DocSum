// src/components/Upload.tsx

import React, { useState, ChangeEvent } from "react";

interface UploadResponse {
  file: string;
  data?: {
    file_id: string;
  };
  error?: string;
}

function Upload() {
  const [files, setFiles] = useState<FileList | null>(null);
  const [responses, setResponses] = useState<UploadResponse[]>([]);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFiles(e.target.files);
  };

  const handleUpload = async () => {
    if (!files) return;

    const uploadedResponses: UploadResponse[] = [];

    for (const file of Array.from(files)) {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch("http://localhost:8000/upload", {
          method: "POST",
          body: formData,
        });

        const data = await response.json();
        uploadedResponses.push({ file: file.name, data });
      } catch (error: any) {
        console.error("Error uploading file:", file.name, error);
        uploadedResponses.push({ file: file.name, error: error.message });
      }
    }

    setResponses(uploadedResponses);
  };

  return (
    <div className="max-w-md mx-auto my-10 p-5 border rounded shadow">
      <h2 className="text-2xl font-bold mb-4">Upload Documents</h2>
      <input
        type="file"
        multiple
        onChange={handleFileChange}
        className="block w-full text-sm text-gray-500
          file:mr-4 file:py-2 file:px-4
          file:rounded file:border-0
          file:text-sm file:font-semibold
          file:bg-blue-50 file:text-blue-700
          hover:file:bg-blue-100"
      />
      <button
        onClick={handleUpload}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Upload
      </button>

      {responses.length > 0 && (
        <div className="mt-6">
          <h3 className="text-xl font-semibold mb-2">Upload Results:</h3>
          <ul>
            {responses.map((res, index) => (
              <li key={index} className="mb-2">
                <strong>{res.file}:</strong>{" "}
                {res.error ? (
                  <span className="text-red-500">{res.error}</span>
                ) : (
                  <span className="text-green-500">
                    Uploaded successfully. File ID: {res.data?.file_id}
                  </span>
                )}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default Upload;
