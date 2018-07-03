"""
URL mappings for edX Proctoring Server.
"""

from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import patterns, url, include

from edx_proctoring import views, callbacks

urlpatterns = patterns(  # pylint: disable=invalid-name
    '',
    url(
        r'edx_proctoring/v1/proctored_exam/exam$',
        views.ProctoredExamView.as_view(),
        name='edx_proctoring.proctored_exam.exam'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/exam/exam_id/(?P<exam_id>\d+)$',
        views.ProctoredExamView.as_view(),
        name='edx_proctoring.proctored_exam.exam_by_id'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/exam/course_id/{}/content_id/(?P<content_id>[A-z0-9]+)$'.format(
            settings.COURSE_ID_PATTERN),
        views.ProctoredExamView.as_view(),
        name='edx_proctoring.proctored_exam.exam_by_content_id'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/exam/course_id/{}$'.format(
            settings.COURSE_ID_PATTERN),
        views.ProctoredExamView.as_view(),
        name='edx_proctoring.proctored_exam.exams_by_course_id'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/attempt/(?P<attempt_id>\d+)$',
        views.StudentProctoredExamAttempt.as_view(),
        name='edx_proctoring.proctored_exam.attempt'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/attempt/session/(?P<attempt_id>\d+)$',
        views.StudentProctoredExamAttemptSession.as_view(),
        name='edx_proctoring.proctored_exam.attempt.session'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/attempt/session/list/{}$'.format(settings.COURSE_ID_PATTERN),
        views.StudentProctoredExamAttemptSessionList.as_view(),
        name='edx_proctoring.proctored_exam.attempt.session_list'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/attempt/course_id/{}$'.format(settings.COURSE_ID_PATTERN),
        views.StudentProctoredExamAttemptsByCourse.as_view(),
        name='edx_proctoring.proctored_exam.attempts.course'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/attempt/course_id/{}/search/(?P<search_by>.+)$'.format(
            settings.COURSE_ID_PATTERN),
        views.StudentProctoredExamAttemptsByCourse.as_view(),
        name='edx_proctoring.proctored_exam.attempts.search'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/attempt$',
        views.StudentProctoredExamAttemptCollection.as_view(),
        name='edx_proctoring.proctored_exam.attempt.collection'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/attempt/(?P<attempt_id>\d+)/review_status$',
        views.ProctoredExamAttemptReviewStatus.as_view(),
        name='edx_proctoring.proctored_exam.attempt.review_status'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/{}/allowance$'.format(settings.COURSE_ID_PATTERN),
        views.ExamAllowanceView.as_view(),
        name='edx_proctoring.proctored_exam.allowance'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/allowance$',
        views.ExamAllowanceView.as_view(),
        name='edx_proctoring.proctored_exam.allowance'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/active_exams_for_user$',
        views.ActiveExamsForUserView.as_view(),
        name='edx_proctoring.proctored_exam.active_exams_for_user'
    ),
    url(
        r'edx_proctoring/v1/proctored_exam/attempt/(?P<attempt_code>[-\w]+)$',
        views.StudentProctoredExamAttemptByCode.as_view(),
        name='edx_proctoring.proctored_exam.attempt'
    ),
    #
    # Unauthenticated callbacks from SoftwareSecure. Note we use other
    # security token measures to protect data
    #
    url(
        r'edx_proctoring/proctoring_poll_status/(?P<attempt_code>[-\w]+)$',
        callbacks.AttemptStatus.as_view(),
        name='edx_proctoring.anonymous.proctoring_poll_status'
    ),
    url(
        r'edx_proctoring/proctoring_launch_callback/start_exam/(?P<attempt_code>[-\w]+)$',
        callbacks.start_exam_callback,
        name='edx_proctoring.anonymous.proctoring_launch_callback.start_exam'
    ),
    url(
        r'edx_proctoring/proctoring_review_callback/$',
        callbacks.ExamReviewCallback.as_view(),
        name='edx_proctoring.anonymous.proctoring_review_callback'
    ),
    url(r'^', include('rest_framework.urls', namespace='rest_framework'))
)
