"""
Video processing routes
"""

from flask import Blueprint, request, jsonify
import logging
from services.video_processor import process_video_frame

video_bp = Blueprint('video', __name__)
logger = logging.getLogger(__name__)

@video_bp.route('/process-frame', methods=['POST'])
def process_frame():
    """
    Process a single video frame
    """
    try:
        if 'frame' not in request.files:
            return jsonify({'error': 'No frame provided'}), 400
        
        frame_file = request.files['frame']
        result = process_video_frame(frame_file)
        
        return jsonify({
            'success': True,
            'frame_id': result['frame_id'],
            'timestamp': result['timestamp'],
            'keypoints': result['keypoints'],
            'pose_landmarks': result['pose_landmarks']
        }), 200
    
    except Exception as e:
        logger.error(f"Error processing frame: {str(e)}")
        return jsonify({'error': str(e)}), 500

@video_bp.route('/stream-status', methods=['GET'])
def stream_status():
    """
    Get current streaming status
    """
    return jsonify({
        'success': True,
        'streaming': False,
        'fps': 30,
        'resolution': '640x480'
    }), 200

@video_bp.route('/extract-keypoints', methods=['POST'])
def extract_keypoints():
    """
    Extract pose keypoints from frame
    """
    try:
        if 'frame' not in request.files:
            return jsonify({'error': 'No frame provided'}), 400
        
        frame_file = request.files['frame']
        from services.keypoint_extractor import extract_keypoints as extract
        
        keypoints = extract(frame_file)
        
        return jsonify({
            'success': True,
            'keypoints': keypoints,
            'count': len(keypoints)
        }), 200
    
    except Exception as e:
        logger.error(f"Error extracting keypoints: {str(e)}")
        return jsonify({'error': str(e)}), 500
