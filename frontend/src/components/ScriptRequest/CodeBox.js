import { Textarea } from "../../styles";
import React, { useRef, useEffect } from 'react';

function AutoResizingTextarea({ value, onChange }) {
    const textareaRef = useRef(null);
  
    const adjustHeight = () => {
      const textarea = textareaRef.current;
      if (!textarea) return;
      textarea.style.height = 'inherit'; // Reset height to recalculate
      textarea.style.height = `${textarea.scrollHeight}px`; // Set to scroll height
    };
  
    useEffect(() => {
      adjustHeight();
    }, [value]);
  
    return (
      <Textarea
        ref={textareaRef}
        value={value}
        onChange={e => {
          onChange(e);
          adjustHeight();
        }}
      />
    );
  }
  
  export default AutoResizingTextarea;