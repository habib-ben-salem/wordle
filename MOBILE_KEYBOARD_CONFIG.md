# Mobile Portrait Mode Keyboard Configuration

## Overview

This Wordle application now includes configurable variables for customizing the on-screen keyboard appearance in portrait mode on mobile devices (screens with max-width: 480px).

## Configuration Variables

The following variables can be modified at the top of `wordle.py` (around lines 24-34):

### `MOBILE_PORTRAIT_KEY_GAP`
- **Default**: `"2px"`
- **Description**: Space between keyboard keys
- **Example values**: `"1px"`, `"3px"`, `"5px"`

### `MOBILE_PORTRAIT_KEY_HEIGHT`
- **Default**: `"44px"`
- **Description**: Height of keyboard keys (minimum recommended: 44px for touch targets)
- **Example values**: `"40px"`, `"48px"`, `"50px"`

### `MOBILE_PORTRAIT_KEY_MIN_WIDTH`
- **Default**: `"26px"`
- **Description**: Minimum width of keyboard keys
- **Example values**: `"24px"`, `"28px"`, `"30px"`

### `MOBILE_PORTRAIT_KEY_MAX_WIDTH`
- **Default**: `"32px"`
- **Description**: Maximum width of keyboard keys (prevents keys from becoming too wide)
- **Example values**: `"30px"`, `"35px"`, `"40px"`

### `MOBILE_PORTRAIT_KEY_FONT_SIZE`
- **Default**: `"10px"`
- **Description**: Font size of text inside keyboard keys
- **Example values**: `"9px"`, `"11px"`, `"12px"`

### `MOBILE_PORTRAIT_KEY_PADDING`
- **Default**: `"0 2px"`
- **Description**: Padding inside keyboard keys (vertical horizontal)
- **Example values**: `"0 1px"`, `"0 3px"`, `"2px 4px"`

## How to Modify

1. Open `wordle.py` in a text editor
2. Find the "MOBILE PORTRAIT MODE KEYBOARD CONFIGURATION" section (lines 24-34)
3. Change the values as needed
4. Save the file
5. Restart the Streamlit application

## Example Customization

For larger keys with more spacing:
```python
MOBILE_PORTRAIT_KEY_GAP = "4px"           # More space between keys
MOBILE_PORTRAIT_KEY_HEIGHT = "48px"       # Taller keys
MOBILE_PORTRAIT_KEY_MIN_WIDTH = "28px"    # Wider minimum width
MOBILE_PORTRAIT_KEY_MAX_WIDTH = "36px"    # Wider maximum width
MOBILE_PORTRAIT_KEY_FONT_SIZE = "11px"    # Larger text
MOBILE_PORTRAIT_KEY_PADDING = "0 3px"     # More horizontal padding
```

For compact keys with minimal spacing:
```python
MOBILE_PORTRAIT_KEY_GAP = "1px"           # Minimal space between keys
MOBILE_PORTRAIT_KEY_HEIGHT = "40px"       # Shorter keys (be careful with touch targets)
MOBILE_PORTRAIT_KEY_MIN_WIDTH = "24px"    # Narrower minimum width
MOBILE_PORTRAIT_KEY_MAX_WIDTH = "30px"    # Narrower maximum width
MOBILE_PORTRAIT_KEY_FONT_SIZE = "9px"     # Smaller text
MOBILE_PORTRAIT_KEY_PADDING = "0 1px"     # Less padding
```

## Important Notes

- These settings only affect mobile devices in portrait mode (screens ≤ 480px wide)
- Ensure `MOBILE_PORTRAIT_KEY_HEIGHT` is at least 44px for proper touch target accessibility
- Test your changes on an actual mobile device or using browser developer tools in mobile emulation mode
- The values should include CSS units (px, em, rem, etc.)

## Testing

To test your changes:
1. Run the Streamlit app: `streamlit run wordle.py`
2. Open the app in a browser
3. Use browser developer tools (F12)
4. Toggle device emulation and set viewport to mobile portrait (e.g., 375x667 for iPhone)
5. Verify the keyboard layout looks correct
