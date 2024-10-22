import React from 'react';
import { ScriptItem, SmallParagraph, SmallHeading, Paragraph, DeleteButton, Button } from '../../styles';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import api from '../../api';

const Scripts = ({ script, onOpen, onDelete }) => {
  const formattedDate = new Date(script.updated_at).toLocaleString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric',
  });
  // Prevent the onOpen event from firing when the delete button is clicked

  let formattedDescription = script.description
  if (formattedDescription.length > 100) {
    formattedDescription = formattedDescription.substring(0,100)+"..."
  }

  return (
    <ScriptItem onClick={() => onOpen(script.id)}>
      <SmallHeading>{script.title}</SmallHeading>
      <Paragraph>{formattedDescription}</Paragraph>
      <SmallParagraph>Updated: {formattedDate}</SmallParagraph>
      <DeleteButton onClick={(e) => onDelete(e, script.id)}>
        <FontAwesomeIcon icon={faTrashAlt} />
      </DeleteButton>
    </ScriptItem>
  );
};

export default Scripts;
