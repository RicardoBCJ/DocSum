// src/components/DocumentDetails.tsx

import React from "react";

interface Entity {
  text: string;
  label: string;
}

interface Document {
  file_id: string;
  filename: string;
  summary: string;
  entities: Entity[];
}

interface DocumentDetailsProps {
  document: Document;
  onClose: () => void;
}

function DocumentDetails({ document, onClose }: DocumentDetailsProps) {
  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div className="bg-white p-6 rounded shadow max-w-lg w-full">
        <h3 className="text-xl font-bold mb-4">Document Details</h3>
        <p>
          <strong>Filename:</strong> {document.filename}
        </p>
        <p>
          <strong>File ID:</strong> {document.file_id}
        </p>
        <p className="mt-4">
          <strong>Summary:</strong>
        </p>
        <p>{document.summary}</p>
        <p className="mt-4">
          <strong>Entities:</strong>
        </p>
        <ul className="list-disc pl-5">
          {document.entities.map((entity, index) => (
            <li key={index}>
              {entity.text} - <em>{entity.label}</em>
            </li>
          ))}
        </ul>
        <button
          onClick={onClose}
          className="mt-6 px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700"
        >
          Close
        </button>
      </div>
    </div>
  );
}

export default DocumentDetails;
