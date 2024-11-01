// src/components/Documents.tsx

import React, { useEffect, useState } from "react";
import DocumentDetails from "./DocumentDetails";

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

function Documents() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [selectedDocument, setSelectedDocument] = useState<Document | null>(
    null
  );

  useEffect(() => {
    fetch("http://localhost:8000/documents")
      .then((response) => response.json())
      .then((data) => setDocuments(data))
      .catch((error) => console.error("Error fetching documents:", error));
  }, []);

  return (
    <div className="max-w-3xl mx-auto my-10">
      <h2 className="text-2xl font-bold mb-4">Documents</h2>
      <ul className="list-disc pl-5">
        {documents.map((doc) => (
          <li key={doc.file_id} className="mb-2">
            <button
              onClick={() => setSelectedDocument(doc)}
              className="text-blue-600 hover:underline"
            >
              {doc.filename}
            </button>
          </li>
        ))}
      </ul>

      {selectedDocument && (
        <DocumentDetails
          document={selectedDocument}
          onClose={() => setSelectedDocument(null)}
        />
      )}
    </div>
  );
}

export default Documents;
