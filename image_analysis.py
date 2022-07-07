import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def describe_image(image_path, description):
    # Display the image
    plt.figure(figsize=(8, 8))
    img = Image.open(image_path)
    title = ''
    if len(description.captions) == 0:
        title = 'No caption detected'
    else:
        for caption in description.captions:
            title = title + " '{}'\n(Confidence: {:.2f}%)".format(caption.text, caption.confidence * 100)
    plt.title(title)
    plt.axis('off')
    plt.imshow(img)


def analyze_image(image_path, analysis):
    # Display the image
    fig = plt.figure(figsize=(16, 8))
    fig.add_subplot(1, 2, 1)
    img = Image.open(image_path)

    # Get the caption
    caption_text = ''
    if len(analysis.description.captions) == 0:
        caption_text = 'No caption detected'
    else:
        for caption in analysis.description.captions:
            caption_text = caption_text + " '{}'\n(Confidence: {:.2f}%)".format(caption.text, caption.confidence * 100)
    plt.title(caption_text)

    # Get objects
    if analysis.objects:
        # Draw a rectangle around each object
        for obj in analysis.objects:
            r = obj.rectangle
            bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)
            plt.annotate(obj.object_property, (r.x, r.y), backgroundcolor='magenta')

    # Get faces
    if analysis.faces:
        # Draw a rectangle around each face
        for face in analysis.faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='lightgreen', width=5)
            annotation = 'Person aged approxilately {}'.format(face.age)
            plt.annotate(annotation, (r.left, r.top), backgroundcolor='lightgreen')

    plt.axis('off')
    plt.imshow(img)

    # Add a second plot for addition details
    a = fig.add_subplot(1, 2, 2)

    # Get ratings
    ratings = 'Ratings:\n - Adult: {}\n - Racy: {}\n - Gore: {}'.format(analysis.adult.is_adult_content,
                                                                        analysis.adult.is_racy_content,
                                                                        analysis.adult.is_gory_content, )

    # Get tags
    # This code returns a tag (key word) for each thing in the image.

    tags = 'Tags:'
    if len(analysis.tags) == 0:
        print("No tags detected.")
    for tag in analysis.tags:
        tags = tags + '\n - {} with confidence {:.2f}%'.format(tag.name, tag.confidence * 100)

    # Print details

    details = '{}\n\n{}'.format(ratings, tags)
    a.text(0, 0.4, details, fontsize=12)
    plt.axis('off')
    plt.show()
